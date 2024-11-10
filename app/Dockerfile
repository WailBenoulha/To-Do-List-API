FROM python:3.12
ENV PYTHONUNBUFFERED=1

# Create the app directory before copying
WORKDIR /app

# Copy only the requirements file first to leverage Docker's caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project to /app
COPY . .

# Expose the port
EXPOSE 8000

# Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["run.sh"]