.PHONY: all task1 task2 task3 clean

all : task1 task2 task3
	
task1:
	(python3 mapper1.py ./chatLogs/day1.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day2.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day3.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day4.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day5.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day6.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day7.txt | sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day8.txt | sort -k 1 -k 2 -n| python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day9.txt |sort -k 1 -k 2 -n | python3 combiner1.py \
	&& python3 mapper1.py ./chatLogs/day10.txt |sort -k 1 -k 2 -n | python3 combiner1.py ) \
	| sort -k 1 -k 2 -n | python3 reducer1.py > network.txt

	@echo "	"
	@echo "network.txt is created..!"
	@echo "	"
	
task2:
	python3 mapper2.py network.txt|sort -k 1 -k 2 -k 3|python3 reducer2.py>friends.txt

	@echo "	"
	@echo "friends.txt is created..!"
	@echo "	"
	
task3:
	python3 mapper3.py network.txt friends.txt|sort -k 1 -k 2 -k 3|python3 reducer3.py>triangles.txt

	@echo "	"
	@echo "triangles.txt is created..!"
	@echo "	"

clean:
	@echo "Cleaning up..."
	rm network.txt
	rm friends.txt
	rm triangles.txt
	
