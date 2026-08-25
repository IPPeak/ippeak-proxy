package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"time"
)

func main() {
	proxyHost := "YOUR_PROXY_HOST"
	proxyPort := "YOUR_PROXY_PORT"
	username := "YOUR_PROXY_USERNAME"
	password := "YOUR_PROXY_PASSWORD"

	proxyURL, err := url.Parse(
		fmt.Sprintf(
			"http://%s:%s@%s:%s",
			username,
			password,
			proxyHost,
			proxyPort,
		),
	)
	if err != nil {
		panic(err)
	}

	client := &http.Client{
		Transport: &http.Transport{
			Proxy: http.ProxyURL(proxyURL),
		},
		Timeout: 30 * time.Second,
	}

	resp, err := client.Get("https://httpbin.org/ip")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println("Proxy IP:")
	fmt.Println(string(body))
}
