FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Add a lint command
RUN echo '#!/bin/bash\nflake8 .\nblack --check .\n' > /usr/local/bin/lint && \
    chmod +x /usr/local/bin/lint

# Add a format command
RUN echo '#!/bin/bash\nblack .\n' > /usr/local/bin/format && \
    chmod +x /usr/local/bin/format

CMD ["python", "app.py"]