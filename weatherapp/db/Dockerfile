# Use the official MySQL image as the base image
FROM mysql:8.0

# Set environment variables for MySQL database configuration
ENV MYSQL_DATABASE=edoudatabase
ENV MYSQL_USER=s5edouard
ENV MYSQL_PASSWORD=s5edouard
ENV MYSQL_ROOT_PASSWORD=s5edouard

# Copy SQL scripts to initialize the database (if needed)
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306
