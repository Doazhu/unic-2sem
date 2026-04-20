package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
)

func main() {
	file, err := os.Open("logs.txt")

	if err != nil {
		fmt.Println("не смог открыть файл:", err)
		return
	}

	defer file.Close()
	pattern := `(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+--\s+\[([^\]]+)\]\s+"(\w+)\s+(\S+)\s+\S+"\s+(\d{3})\s+(\d+)`

	re := regexp.MustCompile(pattern)
	scanner := bufio.NewScanner(file)

	schetchik := make(map[string]int)

	for scanner.Scan() {
		stroka := scanner.Text()
		result := re.FindStringSubmatch(stroka)
		if result == nil {
			continue
		}

		ip := result[1]
		data := result[2]
		metod := result[3]
		put := result[4]
		status := result[5]
		razmer := result[6]

		fmt.Printf("IP: %s | Дата: %s | Метод: %s | Путь: %s | Статус: %s | Размер: %s\n",
			ip, data, metod, put, status, razmer)

		schetchik[ip] = schetchik[ip] + 1
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("ошибка при чтении файла:", err)
	}

	type ipCount struct {
		ip    string
		count int
	}

	var top []ipCount

	for ip, count := range schetchik {
		top = append(top, ipCount{ip: ip, count: count})
	}

	sort.Slice(top, func(i, j int) bool {
		return top[i].count > top[j].count
	})

	fmt.Println("Топ")
	for i, item := range top {
		fmt.Printf("%d. %s - %d раз\n", i+1, item.ip, item.count)
	}

	fmt.Println("гутен")
}
