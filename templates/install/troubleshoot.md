## Troubleshooting Common Problems

In this page we document a set of common problems that users encounter when using their lean toolchain installation. It does not deal with issues that users may encounter with a proof or a language feature. This webpage is a constant Work in Progress. Users who are unable to find a solution to their problems on this page are encouraged to describe their problem on [Zulip](https://leanprover.zulipchat.com/)

### Lost your Infoview

You can get it back as follows
* On a PC or laptop which typically runs windows/linux press `Ctrl+Shift+Enter`
* On an apple machine press `Cmd+Shift+Enter`

### Get Access to Docs inside VSCode

You can get the Lean documentation inside VS Code using `Ctrl-Shift-p` (`Cmd-Shift-p` on MacOS) and then, inside the text field that appears, type `lean doc`` and hit Enter. You will be led to the documentation viewer on a side panel.

### Command Not Found Error on MacOS or Linux
If you encounter any command not found errors when opening a new terminal, try the following quick-fixes in order:
* If you are on macOS and have not tinkered with your shell you are most likely using a shell called `zsh`. Run the command `source ~/.zshrc` and try again.
* If you are on linux, currently the default shell in popular distributions like Ubuntu or Linux Mint is `bash`. In this case, run `source ~/.bashrc`.   
* If this still doesn't work, logging out from MacOS and logging in again should fix it. 

### InitializeSecurityContext error on Windows

Some Windows users have reported an error like this when running lake exe cache get:

>  curl: (35) schannel: next InitializeSecurityContext failed: Unknown error (0x80092012) - The revocation function was unable to check revocation for the certificate

If you see this error, you likely have an antivirus program that scans each downloaded file, which results in errors. Please disable your antivirus program and then run lake exe cache get!. The exclamation mark forces lake to re-download the cache files it failed to download before running this command. (If you are uncomfortable disabling your antivirus, try to follow these instructions and then run lake exe cache get!). You can turn on your antivirus program on afterwards. However, some users also reported that the antivirus programs significantly slow down Lean during normal usage. If Lean is slower than what is expected, either turn off your antivirus program or tell it to ignore/allow the operation of lean.exe.


