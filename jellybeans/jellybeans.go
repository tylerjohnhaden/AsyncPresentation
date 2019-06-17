""" A game that tests your ability to write fast clients. """

package main

import (
    "fmt"
    "log"
    "math"
    "math/rand"
    "net/http"
    "os"
    "strconv"
    "time"
)


var (
    NumberOfJellybeans = 0
    Shuffle = true
    MaxNumberOfJellybeans = int(math.Pow(2, 16))
    Traffic = 0
    MaxTraffic = 0
)



func guess_handler(w http.ResponseWriter, r *http.Request) {
    Traffic++
    guess, err := strconv.Atoi(r.URL.Path[1:])
    
    if err != nil {
        w.WriteHeader(http.StatusNotFound)
        
    } else if guess != NumberOfJellybeans {
        fmt.Fprintf(w, "{\"failure\":%d}", guess)
        
    } else {
        log.Printf("Success! %d jellybeans!\n", guess)
        if Shuffle {
            shuffle_beans()
        }
        fmt.Fprintf(w, "{\"success\":%d}", guess)
    }
}

func shuffle_beans() {
    NumberOfJellybeans = rand.Intn(MaxNumberOfJellybeans)
}

func main() {
    rand.Seed(time.Now().UTC().UnixNano())
    val, ok := os.LookupEnv("JELLYBEAN_COUNT")
    if ok {
        i, err := strconv.Atoi(val)
        if err == nil && i > -1 {
            NumberOfJellybeans = i
            Shuffle = false
        } else {
            shuffle_beans()
        }
    } else {
        shuffle_beans()
    }

    log.Printf("How many jellybeans are in my jar?\n")
    
    go func() {
        TempTraffic := 0
        for {
            time.Sleep(time.Second)
            TempTraffic = Traffic
            Traffic = 0

            if TempTraffic > MaxTraffic {
                MaxTraffic = TempTraffic
            }

            log.Printf("max: %d, cur: %d\n", MaxTraffic, TempTraffic)
        }
    }()
    
    http.HandleFunc("/", guess_handler)
    err := http.ListenAndServe(":7777", nil)
    if err != nil {
        fmt.Errorf("an error occured while running server %s", err.Error())
    }
}
