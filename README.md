# FileSorter
This is a simple file sorter that groups files into folders based on extension
Python 3 is required to use. No external libraries required.

## Usage
###Basic usage
`python3 sort.py -type [path] ([.ext])`

###Advanced usage:
```
Types: -s (sort) -d (display) | -a (append)
 -s  | sort a directory
     | Usage: -s [path] ([.ext])
     | Example(s): -s /Downloads (sorts the entire directory)
     |             -s /Downloads .mp3 .wav .flac (sorts only .mp3 .wav & .flac)
     |
 -d  | display filetypes that can sorted in a directory
     | Usage: -d [path]
     | Example(s): -d /Downloads
     |
 -a  | append extension(s) to the master extensions.txt
     | Usage: -a [.ext1] [.ext2] [.ext3] ...
     | Example(s): -a .txt .docx (adds .txt and .docx to the master extension file)
```

## .bashrc
Type this alias into your `.bashrc` to shortcut sorting a given folder:

> `alias pysort="python3 ~/[PATH TO REPO]/FileSorter/sort.py -s ./"`

Then source the `.bashrc`:

> `source ~/.bashrc`

Now navigate to any folder and type `pysort` to sort into folders.
