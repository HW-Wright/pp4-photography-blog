# Photography Blog
For my fourth Portfolio Project I have decided to create a photography blog, with the purpose of the site being to provide a space for amateur photographers to showcase thier work, away from the noise of social media.

[Please view the live project here!] (https://pp4-photography-blog-dfac9ff0d622.herokuapp.com/)

## User Experience (UX)
### User Stories
----------------------------
#### First Time Visitor Goals
- As a first time visitor, I want to easily be able to perceive the purpose of the site.
- As a first time visitor, I want to have a positive emotional reaction to the site design.
- As a first time visitor, I want to be able navigate the site intuitively.
- As a first time visitor, I want all of the above to be true, regardless of screen size.
#### Returning Visitor Goals
- As a returning time visitor, I want to be able to view the conversations through the comments that are happening underneath the posts.
- As a returning visitor, I want to easily find the page or section that I am looking for.
#### Frequent Visitor Goals
- As a frequent visitor, I want to be able to easily discern the post authors from one another so that I may find the user whom's style I enjoy.
- As a frequent visitor, I want to easily be able to sign up to use the site's full list of features.
#### Verified User Goals
- As a verified user, I want to easily be able to comment on a post.
- As a verified user, I want easily be able to remove a comment I have made.
- As a verified user, I want to be able to upload a post and join the community.
- As a verified user, I want to be able to amend the post for any errors or mistakes.
- As a verified user, I want to easily be able to remove a post if I so choose.
- As a verified user, I want my posts and my comments to be editable or deletable, only by me and site admins.
- As a verified user, I want to log in and log out of the site with ease.

### Development Plan
- This project was organized and executed using Agile methodology. To facilitate this, a Kanban board within GitHub Projects was utilized, with tasks and objectives managed through interconnected GitHub Issues.
[Link to the Kanban Board here](https://github.com/users/blahblahblah589/projects/2)

### Features
----------------------------
#### Existing Features
##### Header
- The header element is identical across all pages of the site. 
- It contains a heading element that acts as the site title and an anchor back to the homepage. This is on the left hand side of the header.
- It also contains a navigation menu to all three pages of the site with the current page the user is on underlined. This is on the right hand side of the header.
#### Hero Image
- The Hero Image, replicated along all pages of the site, depicts photography in action. 
- The header and the subheading overlay the hero image and are also replicated on all site pages
#### index.html
- The site hompage, rendered by the 'index.html' template, contains three sections. 
- The first section shows the three most liked posts on the site at the current time. Here, each post contains the post title, post author, a reduced size version of the post image, the authors caption to the post, how many likes each post has received, along with the location and upload timestamp. All information here is populated my Django from the Post model.
- The second section shows a list of site admins, each with a picture, thier name and a short message for the user. The list is displayed as blocks and is populated by Django from the Editor model.
- The final section of the homepage is a call to action for both verified and non-verified users. If the user is verified, a button will be present to take the user to the AddPost form on 'add_post.html'. If the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'.
#### blog.html
- This page will be populated with every row in the Post model by Django, in order of date created, newer posts appearing at the top.
- Said blog posts will sit inline in rows off three, with any incomplete rows being centered. These blog thumnails contain all the same information as on index.html, but each takes up a smaller section of the page, given that there is far more of them here.
- Just like on index.html, the final section of the blog page is a call to action for both verified and non-verified users. If the user is verified, a button will be present to take the user to the AddPost form on 'add_post.html'. If the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'.
#### specific_post.html
- Here we come to the main purpose of the site, a display of a singluar blog post but a single user. All of the same information is provided as in index.html and blog.html. However, the display is occupying the majority of the viewport to really showcase the image in display.
- This page is where the verified users will get to engage with one another via comments and likes.
- The like icon, unlike in index.html and blog.html, is an interactive button for verified users to like the post. Upon clicking this FontAwesome icon, the page with quickly refresh and display the icon in red.
- The comment secion is displayed for all users, however, the ability to add a comment is soley for verified users. In cases where the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'. If the user is verified they will be able to enter a comment in the provided text area and submit. At this time, the page will again, refresh and display the comment, now with an icon to delete. this icon will take the user to the 'edit_comment.html' template where they can confirm their choice. The user will not be able to edit the comment content so that the flow of conversation cannot be altered after the fact. This option is, of course, not available if the logged in user is not the author of the comment. 
- In cases where a verified user is viewing thier own post, the template will render two significant options below the comments secion. The first of which will be a button link to edit the post, upon submission, the user will be taken to the EditForm displayed on 'edit_post.html' template. Here the user is free to edit the title, caption, location, and status of the post. The slug is not an ediable field because it must always match the title. I have chosen not to allow users to change the image that defines thier post. This decision was made to ensure that no other users' comments would be underneath an imge that they did not see when writing said comment.
#### login.html
- The standard login form template from Django is styles to match the look of the rest of the site. It requests a username and a password, with the option to remember the login.
#### signup.html
- The standard signup form template from Django is styles to match the look of the rest of the site. It requests a username and a password that meets certain criteria.
#### logout.html 
- The standard logout form template from Django is styled to match the look of the site. It simply confirms that this action is desired.
#### Footer
- The footer element is identical across all pages of the site.
- It contains a list element containing anchors to various social media accounts (Instagram, Twitter) and to my GitHub.
- Each link is presented as a FontAwesome icon of each company.
#### Features to be added
- In the future I would like to add a drafts page for verified users, to view the unpublished saved posts that they have created.
- In the future I would like to add the ability for users with a certain amount of points, (as determined by the UserProfile model), to have some form of a 'super-like' functionality. Where they can like and star/emoji a post, I belive this would be a sufficient feature to entice user return.
- Direct links to post authors socal media accounts from the post.
- An embeded Google Maps API that could show you roughly where the picture was taken, if the post auther so choses.

### Design
----------------------------
#### Layout 
##### base.html
- Both the header and footer elements are replicated on all pages of the website.
- ![Header element](/documentation/readme-images/header-pp4.jpeg)
- ![Footer element](/documentation/readme-images/footer-pp4.jpeg)
##### index.html
- The site homepage lists the three most liked posts on the blog. As well as a list of the site admins. 
- ![Featured post](/documentation/readme-images/featured-post-pp4.jpeg)
- ![Admins](/documentation/readme-images/editor-section-pp4.jpeg)
- Followed by a chance for verified users to add a post, and unverified users to sign in or create an account.
- ![Add post button](/documentation/readme-images/add-post-pp4.jpeg)
- ![Call to action](/documentation/readme-images/call-to-action-pp4.jpeg)
##### blog.html
- The main page of the site is the blog page, which shows all the published blog posts in a grid. Followed by a chance for verified users to add a post, and unverified users to sign in or create an account.
- ![Blog](/documentation/readme-images/blog-pp4.jpeg)
##### specific_post.html
- The post page consists of the same details as the previous pages but one post per page.
- ![Specific post](/documentation/readme-images/specific-post-pp4.jpeg)
- The comment section of this page is different for verified and non-verified users, the former having the ability to contribute.
- ![Verified comment section](/documentation/readme-images/comment-section-verified-pp4.jpeg)
- ![Unverified comment section](/documentation/readme-images/unverified-comment-section-pp4.jpeg)
##### add_post.html
- Add post uses crispy forms to generate a the PostForm, which consists of several input fields.
- ![Add post](/documentation/readme-images/create-post-pp4.jpeg)
##### delete_post.html
- This page acts as a confirmation for the desired outcome.
- ![Delete post](/documentation/readme-images/delete-post.jpeg)
#### Color Scheme
- The colour scheme was decided upon for the sake of constrast, red and black was the initial design choice but I amended the background colour gradiend to rgb(171,53,16) so that the hero image remained consistent with site background.

### Wireframes
----------------------------
- My handdrawn wireframes provided a sufficient design model to work from, from the very beggining of the project. So much so that very little has changed from the original design to the live project.
- ![index.html-wireframe-pp4](/documentation/readme-images/wireframe2-pp4.jpeg)
- ![blog.html-wiregrame-pp4](/documentation/readme-images/wireframe1-pp4.jpeg)
- ![specific-post.html-wireframe-pp4](/documentation/readme-images/wireframe3-pp4.jpeg)
- ![add_post.html-wireframe-pp4](/documentation/readme-images/wireframe4-pp4.jpeg)

### Model Design
----------------------------
- Along with the Django User model, and the Post and Comment models that are heavily influenced by the walkthrough project, my project has two custom models. 'UserProfile' and 'Editor'. 
- Entity Relationship Diagram - UserProfile:
- ![ERD - UserProfile](/documentation/readme-images/userprofile-pp4.jpeg)
- Entity Relationship Diagram - Editor:
- ![ERD - Editor](/documentation/readme-images/editor-pp4.jpeg)
- Entity Relationship Diagram - Post:
- ![ERD - Post](/documentation/readme-images/post-model-pp4.jpeg)
- Entity Relationship Diagram - Comment:
- ![ERD - Comment](/documentation/readme-images/comment-model-pp4.jpeg)


## Testing
### Automated Testing
----------------------------
- All tests in the t'test_forms.py', 'test_views.py', test_models.py' pass with no errors.
- ![Automated testing](/documentation/readme-images/auto-testing-pp4.jpeg)

### Additional Testing
----------------------------
- I have tested that this site works on macOS (Ventura 13.2).
- I have tested that this site works on Chrome, Safari, and Brave browsers.
- I have tested that this site works and responds to a mobile devise (iPhone 13 Pro).
- All external links open in a new tab.
- The add post form generates a new post in the blog.
- The comment form refreshes the page with the new comment.
- The like button refreshes the page with an updated like count.
- Deleting a comment refreshes the page with the comment removed, and the option to do so is only available to the comment creator.
- Each post can be updated and deleted, and the option is only available to the post creator.
- Signing out works as desired, the user can no longer engage with the posts or comments, simply view.
- Signing up to the site sucessfully creates a user instance in the Django user model.
- The site is fully responsive from 400pc vw to 2500vw.

### Validators
----------------------------
- The CSS in this projject was validated with no errors.
- ![CSS validation](/documentation/readme-images/css-validator-pp4.jpeg)
- The HTML in this project was validated with no errors:
- ![index.html validation](/documentation/readme-images/index.html-validator-pp4.png)
- ![blog.html validation](/documentation/readme-images/blog.html-validator-pp4.png)
- ![specific_post.html validation](/documentation/readme-images/specific_post.html-validator-pp4.png)
- ![edit_post.html validation](/documentation/readme-images/edit_post.html-validator-pp4.png)
- ![add_post.html validation](/documentation/readme-images/add_post.html-validator-pp4.png)
- ![delete_post.html validation](/documentation/readme-images/delete_post.html-validator-pp4.png)

### Performance and Accesibility
----------------------------
#### Lighthouse
- ![Lightouse score](/documentation/readme-images/lighthouse-pp4.png)

## Technologies Used
- HTML5
- CSS3
- Python3
- Django
- CrispyForms
- ElephantSQL
- Heroku
- Boostrap
- Gunicorn
- Cloudinary
- FontAwesome
- Google Fonts

## Deployment
### This Project was deployed to Heroku
----------------------------
- ![Heroku app](/documentation/readme-images/heroku-pp4.png)
- The below congig vars are required:
- ![Config vars](/documentation/readme-images/config-vars-pp4.png)
- The below buildpacks are required:
- ![Buildpacks](/documentation/readme-images/heroku-buildbacks-pp4.png)
### The media in this project was stored using Cloudinary
----------------------------
- ![Cloudinary](/documentation/readme-images/cloudinary-pp4.png)
### ElephantSQL was used for this project and set up using the steps below
----------------------------
- ![ElephantSQL](/documentation/readme-images/elephantsql-pp3.png)

## Credits
### Content
----------------------------
- Boostrap's clean blog thmese was used as a basis for the besign layout of this project. The usage of this has been clearly labelled in the HTML and CSS.
- The Post and Comment models are heavily influenced by the like models inthe walkthrough project.
- The views that enable comment and like functionality are heavily influenced by the walkthough project.

### Media
----------------------------
- The Hero Image was taken from Unsplash, stock image site.
- The Editor photos were generated using MidJourney.
- All other images are my own.

## Acknowledgments
Brian Macharia, my Code Institue mentor.
The student support systems at Code Institute particularly the tutors. 