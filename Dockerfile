FROM python:3.10-slim

ENV POETRY_VERSION=1.4.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

# Install Poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get install -y unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc \
    && apt-get install --reinstall build-essential -y \
    && apt-get install -y graphviz graphviz-dev \
    && echo "[ODBC Driver 18 for SQL Server]\n\
    Description=Microsoft ODBC Driver 18 for SQL Server\n\
    Driver=/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.0.so.1.1\n\
    UsageCount=1\n\
    " > /etc/odbcinst.ini

# Set environment variables for Graphviz
ENV CFLAGS="-I/usr/include/graphviz" \
    LDFLAGS="-L/usr/lib/graphviz"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev --no-ansi --no-interaction && \
    rm -rf /root/.cache/pypoetry

COPY src ./

CMD ["python", "main.py"]