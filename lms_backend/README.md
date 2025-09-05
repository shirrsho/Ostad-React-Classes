# LMS Backend - Docker Setup

This Django LMS (Learning Management System) backend is fully containerized with Docker and PostgreSQL.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (to clone the repository)

## Quick Start

1. **Clone and navigate to the project:**
   ```bash
   git clone <repository-url>
   cd lms_backend
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Open your browser and go to `http://localhost:8000`
   - The Django development server will be running

## Project Structure

```
├── Dockerfile              # Python/Django container configuration
├── docker-compose.yml      # Multi-container setup (web + database)
├── entrypoint.sh           # Container startup script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── manage.py              # Django management script
├── lms_backend/           # Django project settings
├── core/                  # Core app (courses, lessons, etc.)
├── users/                 # User management app
└── templates/             # HTML templates
```

## Environment Variables

The `.env` file contains configuration for the application:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=*
DATABASE_NAME=lms_db
DATABASE_USER=lms_user
DATABASE_PASSWORD=lms_pass
DATABASE_HOST=db
DATABASE_PORT=5432
```

## Services

### Web Service (Django)
- **Port:** 8000
- **Database:** PostgreSQL
- **Framework:** Django 5.2.6
- **Features:** 
  - Auto-migration on startup
  - File watching for development
  - Volume mounting for live code changes

### Database Service (PostgreSQL)
- **Port:** 5432
- **Database:** lms_db
- **User:** lms_user
- **Persistent storage:** Docker volume `postgres_data`

## Development Commands

**Stop the containers:**
```bash
docker-compose down
```

**View logs:**
```bash
docker-compose logs web    # Web container logs
docker-compose logs db     # Database container logs
```

**Run Django management commands:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic
```

**Access the database:**
```bash
docker-compose exec db psql -U lms_user -d lms_db
```

## Features

- **User Management:** Custom user model with student/teacher roles
- **Course Management:** Create and manage courses with lessons
- **Material Upload:** Support for course materials and lesson videos
- **Responsive Design:** Bootstrap-based templates
- **Media Handling:** File uploads for course banners, videos, and materials

## Production Notes

For production deployment:

1. **Update environment variables:**
   - Set `DEBUG=False`
   - Use a strong `SECRET_KEY`
   - Configure `DJANGO_ALLOWED_HOSTS` properly

2. **Use production database:**
   - Consider managed PostgreSQL service
   - Update database credentials

3. **Enable HTTPS:**
   - Use a reverse proxy (nginx)
   - Configure SSL certificates

4. **Static files:**
   - Uncomment `collectstatic` in Dockerfile
   - Configure static file serving

## Troubleshooting

**Container won't start:**
- Check if ports 8000 and 5432 are available
- Verify Docker and Docker Compose are installed correctly

**Database connection issues:**
- Wait for PostgreSQL to fully start (entrypoint.sh handles this)
- Check database credentials in .env file

**Permission errors:**
- Ensure entrypoint.sh is executable: `chmod +x entrypoint.sh`

## Support

For issues and questions, please check the logs:
```bash
docker-compose logs -f
```
