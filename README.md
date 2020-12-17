## debito_automatico

avaliação backend T10


# ------------ Não usar em produção ------------





## Tecnologias
- Linguagem: [Python](https://www.python.org/)
- API framework - [FastApi](https://fastapi.tiangolo.com/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/link)
- Banco de dados relacional: [PostgreSQL](https://www.postgresql.org/) e [pgAdmin](https://www.pgadmin.org/)
- Migrações: [Alembic](https://alembic.sqlalchemy.org/en/latest/link)
- Tarefas: [Celery](https://pypi.org/project/celery/) e [Flower](https://flower.readthedocs.io/en/latest/)
- Broker: [RabbitMQ](https://www.rabbitmq.com/)
- Cache: [Redis](https://redis.io/)




## Como rodar o projeto
- Clone com git
`git clone https://github.com/ralphribeiro/debito_automatico.git`

- Constrói containers
`docker-compose build`

- Aplica migração
`docker-compose run --rm backend alembic upgrade head`

- Aplica dados iniciais
`docker-compose run --rm backend python3 app/initial_data.py`

- Sobe containers
`docker-compose up -d`

- Roda testes
`docker-compose run backend pytest`





## End points

[Docs](http://localhost:8000/api/v1/docs)




### Suporte

[pgAdmin](http://localhost:5050/)

[Flower](http://localhost:5555/)


