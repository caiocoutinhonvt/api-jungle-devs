# Jungle Devs Challenge ###001


Jungle-Devs Challenge, a challenge to get a general understanding of how an API works, made in Django REST Framework
## Install


Run these commands in your terminal:

```bash
  make build

  inside make build contains:
  	docker exec web pip install -r requirements.txt
	docker exec web pip install --upgrade pip
	docker exec web python3 manage.py migrate
```


```bash
  make up

  inside make up contains:
  	docker-compose up
```



    
## API Documentation

### Articles ### 


### Admin end-point Articles 

```
  GET /api/admin/articles/
```


#### Return All Articles

```
  GET /api/articles/
```


#### Return Articles for ID

```
  GET /api/articles/${id}
```
#### Create Articles

```
  POST /api/admin/articles/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `author_id` | `string` | **Mandatory**|
| `category` | `string` | **Mandatory**|
| `title` | `string` | **Mandatory** |
| `summary` | `string` | **Mandatory** |
| `firstParagraph` | `string` | **Mandatory** |
| `body` | `string` | **Mandatory (50 characters minimum)**|

#### Edit Articles (pass all parameters)

```
  PUT /api/admin/articles/${id}
```

| Parâmetro   | Tipo       | 
| :---------- | :--------- | 
| `author_id` | `string` | 
| `category` | `string` |
| `title` | `string` |
| `summary` | `string` | 
| `firstParagraph` | `string` |
| `body` | `string` | 

#### Edit Articles (pass parameters individually)

```
  PATCH /api/admin/articles/${id}
```

#### Delete articles 

```
  DELETE /api/admin/articles/${id}
```

### Author 

#### Return All Author

```
  GET /api/admin/authors/
```

#### Return All Author for ID

```
  GET /api/admin/authors/${id}
```


#### Create Author

```
  GET /api/admin/authors/
```
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `author_id` | `string` | **Mandatory**|
| `picture` | `string` | **Mandatory**|



#### Edit Author (pass all parameters)

```
  PUT /api/admin/authors/${id}
```

| Parâmetro   | Tipo       | 
| :---------- | :--------- | 
| `id` | `string` | 
| `name` | `string` |
| `picture` | `file` |


#### Edit Author (pass parameters individually)

```
  PATCH /api/admin/authors/${id}
```

#### Delete articles (pass parameters individually)

```
  DELETE /api/admin/authors/${id}
  ```

### User 

#### Login

```
  POST /api/login/
```

#### Sign-up

```
  POST /api/sign-up/
  ```


































## Documentation 

[Jungle Devs Challenge](https://github.com/JungleDevs/django-challenge-001)

