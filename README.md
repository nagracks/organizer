# Organizer

> `Organizer` is script which helps your organize your files easily.

Usage
-----

```
usage: organizer.py [-h] [-d /full/directory/path]

Organizer

optional arguments:
  -h, --help            show this help message and exit
  -d /full/directory/path, --directory /full/directory/path
                        directory you want to organize
```

TODO
----

`Organizer` is a work in progress, so any ideas and patches are appreciated.

* [x] Somehow make it work
* [ ] Improve folder names
* [ ] Group similar kind of files
    * Documents
    * Videos
    * Audios
    * Compressed
* [ ] Dry run option, shows data in organized way without copying/moving data
    * To do this I am thinking about to make use of symbolic links 
    * Make organized symbolic links to /tmp directory  
    * Make output prettify
    * Show file count of filetypes. Eg. `pdf 700`, `jpg 1200`
* [ ] Make it more flexible to suit everyone's need

Contributing
------------

Feel free to improve `Organizer`. All kinds of pull-requests are welcome.

LICENSE
------

`Organizer` is licensed under 
[GPL3](https://github.com/nagracks/organizer/blob/master/LICENSE)
