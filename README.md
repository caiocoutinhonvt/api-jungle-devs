
# Jungle Devs Challenge ###001


A challenge to get a general understanding of how an API works, made in Django REST Framework. The concepts applied were:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).


## Install


Run these commands in your terminal:

* Install Docker
* Install Docker Compose
* Install Makefile 



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
  GET /api/articles/${id}/
```
#### Create Articles

```
  POST /api/admin/articles/
```

| Parameters   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `author_id` | `string` | **Mandatory**|
| `category` | `string` | **Mandatory**|
| `title` | `string` | **Mandatory** |
| `summary` | `string` | **Mandatory** |
| `firstParagraph` | `string` | **Mandatory** |
| `body` | `string` | **Mandatory (50 characters minimum)**|

#### Edit Articles (pass all parameters)

```
  PUT /api/admin/articles/${id}/
```

|  Parameters   | Type       | 
| :---------- | :--------- | 
| `author_id` | `string` | 
| `category` | `string` |
| `title` | `string` |
| `summary` | `string` | 
| `firstParagraph` | `string` |
| `body` | `string` | 

#### Edit Articles (pass parameters individually)

```
  PATCH /api/admin/articles/${id}/
```

#### Delete articles 

```
  DELETE /api/admin/articles/${id}/
```

### Author 

#### Return All Author

```
  GET /api/admin/authors/
```

#### Return All Author for ID

```
  GET /api/admin/authors/${id}/
```


#### Create Author

```
  GET /api/admin/authors/
```
| Parameters   | Type       | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `author_id` | `string` | **Mandatory**|
| `picture` | `string` | **Mandatory**|



#### Edit Author (pass all parameters)

```
  PUT /api/admin/authors/${id}/
```

| Parameters   | Type       | 
| :---------- | :--------- | 
| `id` | `string` | 
| `name` | `string` |
| `picture` | `file` |


#### Edit Author (pass parameters individually)

```
  PATCH /api/admin/authors/${id}/
```

#### Delete articles (pass parameters individually)

```
  DELETE /api/admin/authors/${id}/
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
  
#### To acess Swagger 

http://0.0.0.0:8000/swagger

  
## Screenshot


<img alt="demoimage" title ="demoimage"  src ='https://user-images.githubusercontent.com/100374964/170395251-99a05ba9-83ba-4312-8c31-34722b304f10.png'/> 






## Documentation 

[Jungle Devs Challenge](https://github.com/JungleDevs/django-challenge-001)


