# 🤖 AI-Powered SEO Blog CMS

A professional Django-based **AI-powered blogging and content management system** that helps users create, manage, optimize, and publish SEO-friendly blog content.

The platform combines **Django, AI content generation, SEO tools, authentication, blog management, comments, bookmarks, and an admin dashboard** into one complete web application.

## 🚀 Live Demo

🌐 **Live Website:** https://ai-blog-cms-web.onrender.com

💻 **GitHub Repository:** https://github.com/Abhishek9793ab/ai-blog-cms

---

## 📌 Project Overview

AI Blog CMS is designed to simplify the complete blogging workflow.

Users can:

* Create and manage blog posts
* Generate blog content using AI
* Optimize articles for SEO
* Add categories and tags
* Upload featured images
* Save drafts
* Publish articles
* Search and filter blogs
* Comment on articles
* Bookmark favorite blogs
* Manage their profile

Administrators can manage blogs, users, comments, categories, tags, and SEO information through the dashboard and Django admin panel.

---

## ✨ Key Features

### 🤖 AI Blog Generator

* Generate complete blog articles using AI
* Generate title and excerpt
* Generate SEO title
* Generate meta description
* Generate focus keyword
* Generate relevant tags
* Generate structured HTML content

### 📝 Blog Management

* Create blogs
* Edit blogs
* Delete blogs
* Draft / Published status
* Featured blog support
* Featured image upload
* Author management
* Publish date tracking

### 🔍 SEO Optimization

* SEO title
* Meta description
* Focus keyword
* Canonical URL
* SEO audit score
* Content depth check
* Featured image check
* Category and tag checks
* XML sitemap
* Robots.txt
* Related blog posts

### 👤 Authentication

* User registration
* Login
* Logout
* User profile
* Profile update
* Authentication-protected features

### 💬 Comments

* Users can comment on blogs
* Comment moderation
* Pending comments
* Approved comments
* Rejected comments
* Admin comment management

### 🔖 Bookmarks

* Save favorite blogs
* Remove bookmarks
* User-specific bookmarks

### 📊 Dashboard

The custom dashboard provides:

* Total blogs
* Published blogs
* Draft blogs
* Total views
* Total users
* Total comments
* Pending comments
* Categories
* Tags
* Recent blogs
* SEO audit information

---

## 🛠️ Tech Stack

### Backend

* Python
* Django 6.1.1
* Django ORM
* SQLite
* PostgreSQL support

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### AI

* Google Gemini API
* REST API integration

### Libraries & Tools

* Pillow
* Requests
* python-dotenv
* WhiteNoise
* Gunicorn
* dj-database-url
* Psycopg

### Deployment

* Render
* GitHub

---

## 📂 Project Structure

```text
ai-blog-cms/
│
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   ├── ai_service.py
│   ├── seo.py
│   ├── utils.py
│   └── sitemaps.py
│
├── accounts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── dashboard/
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── blog/
│   ├── accounts/
│   └── dashboard/
│
├── static/
│   ├── css/
│   └── js/
│
└── media/
    ├── blogs/
    └── profiles/
```

---

## 🗃️ Database Models

The application currently uses the following main models:

### Category

Stores blog categories.

### Tag

Stores blog tags.

### Blog

Stores:

* Title
* Slug
* Content
* Excerpt
* Featured image
* Author
* Category
* Tags
* Status
* SEO information
* Views
* Publish date

### Comment

Stores user comments and moderation status.

### Bookmark

Stores user-specific saved blogs.

---

## 🔐 Environment Variables

Create a `.env` file locally:

```env
DEBUG=True

DJANGO_SECRET_KEY=your-secret-key

ALLOWED_HOSTS=127.0.0.1,localhost

CSRF_TRUSTED_ORIGINS=

GEMINI_API_KEY=your-gemini-api-key

GEMINI_MODEL=gemini-3.6-flash

DATABASE_URL=
```

**Never upload `.env` to GitHub.**

The project includes `.gitignore` to protect environment secrets.

---

## 💻 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abhishek9793ab/ai-blog-cms.git
```

### 2. Open the project

```bash
cd ai-blog-cms
```

### 3. Create virtual environment

Windows:

```bash
python -m venv .venv
```

### 4. Activate virtual environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create admin user

```bash
python manage.py createsuperuser
```

### 8. Run development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Admin Panel

The Django admin panel is available at:

```text
/django-admin/
```

Example:

```text
http://127.0.0.1:8000/django-admin/
```

Administrators can manage:

* Blogs
* Categories
* Tags
* Comments
* Bookmarks
* Users

---

## 🌐 Main Application URLs

| Feature       | URL                        |
| ------------- | -------------------------- |
| Home          | `/`                        |
| All Blogs     | `/blogs/`                  |
| Create Blog   | `/create/`                 |
| Login         | `/accounts/login/`         |
| Register      | `/accounts/register/`      |
| Profile       | `/accounts/profile/`       |
| Dashboard     | `/dashboard/`              |
| AI Generator  | `/dashboard/ai-generator/` |
| SEO Dashboard | `/dashboard/seo/`          |
| Sitemap       | `/sitemap.xml`             |
| Robots        | `/robots.txt`              |
| Django Admin  | `/django-admin/`           |

---

## 📈 SEO Features

The project includes a built-in SEO audit system.

The audit checks:

* SEO title length
* Meta description length
* Focus keyword usage
* Blog excerpt
* Featured image
* Category
* Tags
* Content depth

An SEO score is generated based on these checks.

---

## 🚀 Deployment

The project is deployed on **Render**.

Production server uses:

```text
Gunicorn
```

Static files are handled using:

```text
WhiteNoise
```

Production database support is implemented using:

```text
PostgreSQL
```

The deployment configuration includes:

```text
Procfile
requirements.txt
Environment Variables
collectstatic
Django migrations
```

---

## 🔒 Security

The project follows basic Django security practices:

* Secret keys stored in environment variables
* `.env` excluded from Git
* CSRF protection
* Secure cookies for production
* HTTPS support
* X-Frame-Options protection
* Environment-based configuration

---

## 🧪 Project Testing

Before deployment, the project was checked using:

```bash
python manage.py check
```

Static files were tested using:

```bash
python manage.py findstatic css/style.css
python manage.py findstatic js/main.js
```

Production static files were collected using:

```bash
python manage.py collectstatic --noinput
```

---

## 🎯 Future Improvements

Possible future improvements include:

* Advanced visitor analytics
* Unique visitor tracking
* Google Analytics integration
* AI-powered SEO recommendations
* AI image generation
* Social media sharing automation
* Email notifications
* PostgreSQL production migration
* Persistent media storage
* Advanced search
* Blog reading-time calculation
* Related-content recommendations

---

## 👨‍💻 Developer

**Abhishek Prajapati**

B.Tech Computer Science & Engineering — 2026

### Skills

* Python
* Django
* SQL
* Machine Learning
* Deep Learning
* Generative AI
* LLM
* Data Science
* HTML
* CSS
* JavaScript
* Bootstrap
* Git & GitHub

---

## ⭐ Project Highlights

This project demonstrates practical knowledge of:

**Django + Python + REST API + Generative AI + SEO + Authentication + CRUD + Database + Dashboard + Deployment**

It was built as a complete web application rather than a simple AI script or static website.

---

## 📄 License

This project is created for educational, portfolio, and demonstration purposes.
