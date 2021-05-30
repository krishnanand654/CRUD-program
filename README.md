# Description

CRUD operation on files using python.
File named `data.txt` will act as database for this program.

# **CRUD**

create, read, update, and delete (CRUD) are the four basic operations of persistent storage. Alternate words are sometimes used when defining the four basic operations of CRUD, such as construct instead of create, retrieve instead of read, or destroy or destruct instead of delete.

* CREATE procedures: Performs the INSERT operation to create a new record.

* READ procedures: READS the file records based on the ID.

* UPDATE procedures: UPDATES records on the table based on the ID.

* DELETE procedures: DELETES a specified row based on the ID.

Most applications have some form of CRUD functionality. In fact, every programmer has had to deal with CRUD at some point. Not to mention, a CRUD application is one that utilizes forms to retrieve and return data from a database.


# **File Handling**

## Opening Files in Python

Python has a built-in `open()` function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

There are four different methods (modes) for opening a file:

* "r" - Read - Default value. Opens a file for reading, error if the file does not exist

* "a" - Append - Opens a file for appending, creates the file if it does not exist

* "w" - Write - Opens a file for writing, creates the file if it does not exist

* "x" - Create - Creates the specified file, returns an error if the file exists

## Closing Files in Python

When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the `close()` method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.
