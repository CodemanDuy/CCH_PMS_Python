# ENTITIES NOTE

Instruction to structure the entities folder

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

NOT ALLOW to add any files which is not entity model into this folder because it will break the unit test 

```
ProcessAccount.py: => NOT ALLOWED: this class not belong to any table in Database
Account.py: => ALLOWED: this class match with a table in Database
```

All Entity Model class must be named exactly the same as Table Name in Database with no prefix or suffix

```
Account, Property, etc
```


All attributes in Entity Model class must match exactly the same name as Table Column name in Database 

```
Account Table: [AccountId, Fullname, etc...]
Account Class: [AccountId, Fullname, etc...]
```

## Running the tests

Try to run code in class "testcase_entity.py" in "unit_test" folder

### test_entitycontainer_size()

Compare the total entity files with ".py" in entity

```

```

### test_entitycontainer_registername()

Check out the entity class not registed in EntityContainer class by comparing with files in "entities" folder

```

```