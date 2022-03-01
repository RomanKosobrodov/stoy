# stoy
Application for shutting down kernels in Jupyter Lab after they were idle for a specified period of time.
The jupyter instance itself is terminated when no kernels were open for some time.


# Usage

Add the following to `on_start.sh` script of your Sagemaker instance:
```commandline
pip install stoy
export TOKEN=`generate-token`
echo -e '\nc.NotebookApp.token="'$TOKEN'"\n' >> /home/ec2-user/.jupyter/jupyter_notebook_config.py 
stoy --kernel-idle=3600 --server-idle=1800 --token=$TOKEN --url="https://localhost:8443" --log="/var/log" &
```
`generate-token` is a script installed with `stoy` that uses `uuid.uuid4` to generate a unique token. The token is saved in 
an environment variable. The `echo` command adds the token to Jupyter notebook configuration file. Finally,
`stoy` is started as a background script and the token is passed to it.


# Troubleshooting

The application saves logs in `stoy.log` located in the directory specified by the `--log` argument.
The default location is `~/.stoy/stoy.log`.  
To access the logs open jupyter lab terminal and run `tail`, for example:
```commandline
tail -f /var/log/stoy.log
```
or 
```commandline
tail -f ~/.stoy/stoy.log
```
Use `Control-C` to stop watching the logs.