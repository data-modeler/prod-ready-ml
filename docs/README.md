# prod_ready_ml
<!-- prod_ready_ml documentation -->
# Make Dataset

Creates the database tables from csv files to be used in training.


### src.data.make_dataset.load_data_to_db(input_filepath: str)
Creates database table(s) from raw data.

**NOTE**: The database uri should be in the environment as DB_URI. See the
.env_example for an example of how to structure the .env file.


* **Parameters**

    **input_filepath** – The directory of the raw csv files to be loaded into
    the database.



* **Returns**

    None

<!-- prod_ready_ml documentation -->
# Train Model

Runs the training for the model.


### src.models.train_model.sample(x: int = 1, letters: str = 'ABC')
Is a sample function.

**NOTE**: This is an example of complete documentation.


* **Parameters**

    
    * **x** – The first value to pass in.


    * **letters** – The second argument.



* **Returns**

    True if acceptable; False if unacceptable



* **Raises**

    **ValueError** – if x is not int or letters is not string


### Examples

```python
>>> print(sample(3, ' is the number'))
'3 is the number'
```

