# https://www.hackerrank.com/challenges/simple-array-sum
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/ruby

n = gets.strip.to_i
arr = gets.strip
puts arr.split(' ').map(&:to_i).inject(0){|n, i| n + i}

