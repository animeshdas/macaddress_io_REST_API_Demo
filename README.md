# macaddress.io - REST API Demo



check_mac.py is a Python program, that demos a simple REST API to talk to [macaddress.io](https://www.macaddress.io) REST API services to check the name of the company holding ownership of any mac address. 



## Prerequisite

Tested on 



- [CentOS 7.4](https://www.centos.org/)

- [Python 2.7](https://www.python.org)

- [PIP 19.2.1](https://pip.pypa.io)

- [Request 2.20.1](https://pypi.org/project/requests/)





## Installation



Use [Git](https://git-scm.com/) clone to clone this repository.



```git

git clone <this repo url>

cd <cloned dir>

```



## Standalone Usage



Install you macaddress.io API key.

```bash

cd assets

chmod 755 install_apikey.sh

./install_apikey.sh

mv macaddress_io.apikey ../.

```



Run the python program

```python

python check_mac.py

```



<span style="color: red"> :red_circle: **For Security reasons, delete the API key once you are done.** </span>



```bash

rm -rf macaddress_io.apikey

```





## Docker Usage



Build your image once with API Key

```bash

chmod 755 build.sh

./build.sh

```



Run the python program

```bash

chmod 755 build.sh

./run.sh

```



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. You can also drop me an email at _jobs4ani at gmail dot com_


# SECURITY
To secure the API-Key, gnome-keyring along with python-keyring in headless mode (without X), can be used to store the API Key. But this is out of scope for now, due to time constraint.


## License

[MIT](https://choosealicense.com/licenses/mit/)
