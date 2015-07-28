package main

import (
	"time"
	"sync"
)

func snooze(){
	time.Sleep(time.Second * 10)
}

func main(){
	var mainSync sync.WaitGroup
	for i := 0; i < 10000; i++ {
		mainSync.Add(1)
		go func(){
			defer mainSync.Done()
			snooze()
		}()
	}
	mainSync.Wait()
}
