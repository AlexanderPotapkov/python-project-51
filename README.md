# Page loader

[![Actions Status](https://github.com/AlexanderPotapkov/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/AlexanderPotapkov/python-project-51/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/0e7d57ed4a01c6d2ee27/maintainability)](https://codeclimate.com/github/AlexanderPotapkov/python-project-51/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/0e7d57ed4a01c6d2ee27/test_coverage)](https://codeclimate.com/github/AlexanderPotapkov/python-project-51/test_coverage)

Page loader is a utility for downloading a page from the web. It downloads resources from the same domain as specified in the URL and saves them by changing the path in the HTML document.

### Installation
```
    pip install "git+https://github.com/AlexanderPotapkov/python-project-51.git"
```
<a href="https://asciinema.org/a/535109" target="_blank"><img src="https://asciinema.org/a/535109.svg" /></a>

### For help
```
    page-loader --help
```
<a href="https://asciinema.org/a/535110" target="_blank"><img src="https://asciinema.org/a/535110.svg" /></a>

### To run the utility
The downloaded HTML page is saved by default 'os.getcwd()'
```
    page-loader name-of-website
```
<a href="https://asciinema.org/a/537274" target="_blank"><img src="https://asciinema.org/a/537274.svg" /></a>
If the --output flag is specified, then after it you need to specify the path to the desired directory. If the directory does not exist, it will be created.
```
    page-loader --output name-of-directory name-of-website
```
<a href="https://asciinema.org/a/537276" target="_blank"><img src="https://asciinema.org/a/537276.svg" /></a>
