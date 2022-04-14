from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
#imports we need from our models
from app.models import db, Customer, Post
from .blogforms import PostForm
from flask_login import current_user, login_required

blog=Blueprint('blog', __name__, template_folder='blog_templates', url_prefix='/blog')

# The 4 scenarios I need to cover in my templating/conditionals is-1.)The user doesn't exist, this is my page, this
#is someone elses page and im logged in or this is somebody elses page and i'm logged out

@blog.route('/<string:username>', methods=['GET', 'POST'])
def userProfile(username):
    customer = Customer.query.filter_by(username=username).first()
    if customer:
        posts = Post.query.filter_by(customer_id=customer.id).order_by(Post.timestamp.desc()).all()
    else:
        # replace with 404 redirect later
        #return redirect(url_for404)
        return render_template('userprofile.html', customer=None, posts=None)
    # if we get here, a customer exists with this customername
    form = PostForm()
    if request.method == 'POST' and current_user.is_authenticated:
        if current_user.id == customer.id and form.validate_on_submit():
            # normal post stuff
            newpost = Post()
            newpost.body = form.new_post.data
            newpost.customer_id = current_user.id
            db.session.add(newpost)
            db.session.commit()
            flash('New post created :)', 'success')
            return redirect(url_for('blog.userProfile', username=current_user.username))
        else:
            # someone tried to bypass the template, don't let them
            return jsonify({'Come on': 'you shouldnt be here'}), 403
    return render_template('userprofile.html', customer=customer, posts=posts, form=form)


# pretty common structure for a route for a button that does some interaction with database
# has its own route which does some stuff then redirects back to a route that renders a template
@blog.route('/delete/<int:pid>')
@login_required
def deletePost(pid):
    to_delete = Post.query.get(pid)
    if current_user.id == to_delete.customer_id:
        db.session.delete(to_delete)
        db.session.commit()
        flash('Post deleted successfully.', 'info')
        return redirect(url_for('blog.userProfile', username=current_user.username))
    return jsonify({'Come on': 'you shouldnt be here'}), 403

@blog.route('/users')
def users():    
    if current_user.is_authenticated:
        customers = Customer.query.filter(Customer.id!=current_user.id).all()
    else:
        customers = Customer.query.all()
    return render_template('findusers.html', customers=customers)

@blog.route('/newsfeed')
def newsfeed():
    if current_user.is_authenticated:
        # this will change to a different query when we have our follower system built
        posts = current_user.followed_posts()
    else:
        # no one signed in? show all the posts
        posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('newsfeed.html', posts=posts)

@blog.route('/follow/<string:uid>')
@login_required
def follow(uid):
    u = Customer.query.get(uid)
    current_user.follow(u)
    flash(f'Followed @{u.username}', 'info')
    return redirect(url_for('blog.userProfile', username=u.username))

@blog.route('/unfollow/<string:uid>')
@login_required
def unfollow(uid):   
    u = Customer.query.get(uid)
    current_user.unfollow(u)
    flash(f'Unfollowed @{u.username}', 'warning')
    return redirect(url_for('blog.userProfile', username=u.username))