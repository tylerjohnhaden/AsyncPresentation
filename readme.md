# Async Presentation
by: Tyler Haden

See AsyncPresentation.pptx

***

## Jellybean Experiment

I will be running the jellybeans.go server during the 
presentation. Try to guess the 'number of jellybeans in the 
jar' by sending a get request to `10.248.33.45:7777/{int:guess}` 
where `0 <= guess <= 2 ** 16`. Every time someone guesses the right
number of jellybeans, the number reshuffles, and I will reward you 
with jellybeans.

###failed response
```json
{
    "failed": 0
}
```

###successful response
```json
{
    "success": 0
}
```


