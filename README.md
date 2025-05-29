
# proofreader-ai

**proofreader-ai** is an AI-driven proofreading API designed to help developers and teams automatically check and correct grammar, spelling, and clarity in text. Built on FastAPI and leveraging advanced language models, it provides a simple, scalable, and asynchronous REST API for integrating proofreading capabilities into your applications, workflows, or content pipelines.

Key features include:
- Seamless integration with modern AI models *(e.g., OpenAI, GitHub Models)*
- Fast, asynchronous processing for high performance
- Simple RESTful endpoints for easy automation
- Interactive API documentation via Swagger UI and ReDoc
- Secure token-based authentication using environment variables

Whether you are building content management systems, document editors, chatbots, or any application that benefits from high-quality text, **proofreader-ai** offers a robust and extensible solution for automated proofreading.

## :computer: Prerequisites
- Python 3.13 or higher *([Download Python](https://www.python.org/downloads/))*
- Poetry 2.0 or higher *([Poetry installation guide](https://python-poetry.org/docs/#installation))*

## :package: Installation
This project uses [Poetry](https://python-poetry.org/) for dependency management.

```sh
git clone https://github.com/rcw3bb/proofreader-ai.git
cd proofreader-ai
poetry install
```


Create a `.env` file in the project root with your GitHub Models API token:

## :warning: Logging

The project uses a `logging.ini` file for logging configuration. Logs are written to `proofreader-ai.log` and the console. You can adjust logging settings in `logging.ini` at the project root.

```env
GITHUB_TOKEN=your_github_models_token_here
```


## :zap: Usage

You can run the API server with:
```sh
poetry run uvicorn proofreader_ai.server:app
```

Once running, interactive API documentation is available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Sample API Usage

Send a POST request to `/proofread` with your text:

```sh
curl -X POST "http://127.0.0.1:8000/api/v1/proofread" -H "Content-Type: application/json" -d '{"text": "This is a sample paragraf with a typo and bad grammar."}'
```

**Response:**

```json
{
    "messages": [
        {
            "content": "This is a sample paragraph with a typo and poor grammar.",
            "role": "assistant",
            "annotations": [],
            "refusal": null
        }
    ]
}
```

## :wrench: Development
- All source code is in the `proofreader_ai` package.
- Tests are in the `tests` package, mirroring the source structure.

## :microscope: Testing & Coverage
Run all tests and generate an HTML coverage report:
```sh
poetry run pytest --cov=proofreader_ai tests --cov-report html
```
Open `htmlcov/index.html` to view the coverage report.

## :art: Formatting & Linting
Format and lint the code in one step:
```sh
poetry run black proofreader_ai && poetry run pylint proofreader_ai
```

## :scroll: Changelog
See [CHANGELOG.md](CHANGELOG.md) for release history.

## :key: License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## :pen: Author
**Ron Webb**
