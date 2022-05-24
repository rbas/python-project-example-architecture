# Python project architecture example

## Goal
The Goal of this project to show python project architecture what is framework-agnostic and following [DDD](https://www.domaindrivendesign.org) and [Clean Code Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
All application code is in different layers with strict boundaries. That should help with easier reading and future project changes like.
* Change 3rd party API provider, changes will happen in `Persistence` layer, It should not affect business logic.
* Infrastructural changes, they don't affect business logic, it means it should happen in its layer
* Changing framework. For example chosen framework is not support in serverless environments, if project need to be migrated. It should not affect business logic.
* Etc...

All those changes should be more or less easy to do in such architecture chosen in this project. 


### Disclaimer
Project is just for learning purpose to show architecture examples by using [DDD](https://www.domaindrivendesign.org) and [Clean Code Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) principles.
Author didn't mean that chosen solution is silver bullet in software architecture. In software development is none of it.
Even though that project is fully functional not all parts are fully done.

## How to read project
All documentation is written as part of code. Suggested order for reading is following.

1) `entity/entities.py`
2) `entity/valueobject.py`
3) `customtypes/invoice.py`
4) `api.py`
5) `usecases.py`
6) `persistance/repository.py`
7) `persistance/mapper/dummy.py`

## Installation
Project is fully functional, made on top of Python version 3.10. By using [Starlette](https://www.starlette.io/) framework with [Uvicorn](https://www.uvicorn.org) combination.

### Install dependencies

```shell
pip install -r requirements.txt
```

### Run HTTP server
```shell
cd src
uvicorn api:app --reload
```

## Testing

### Run tests

```shell
pytest
```

### Integration tests via HTTP

Integration tests are in `tests.http`

## What next?
The best way how to learn is to practice. Fork this repository and start working with code.
* Finish all missing API endpoints
  * `POST /invoices` is not parsing data from request
  * `GET /invoices` does not exist
  * `PUT /invoices/<id>/mark-as-paid/` does not exist
* Create `Mapper` for persistence storage like: SQL like storages, Filesytem, memory etc...

