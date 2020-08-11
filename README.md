# Propterra
Silly Python site for calculating the opposite side of the Earth from any given point.

To get started, clone the repo and run the following at the commandline:
```powershell
setx Maps_API_Key zzzzzzzAPIkeyvaluezzzzzzz
docker build --build-arg API_KEY=${env:Maps_API_Key} -t propterra:latest .
docker run -p 5000:5000 -d --name propterra propterra:latest
```
_Note: It's not a great idea to bake your API key into the image. Ideally one would be using ```docker secret```._

To peek inside of the container for troubleshooting:
```powershell
docker attach propterra
```
Navigate to http://127.0.0.1:5000/ in your browser.
