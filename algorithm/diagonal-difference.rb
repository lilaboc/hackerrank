# https://www.hackerrank.com/challenges/diagonal-difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/ruby

n = gets.strip.to_i
a = 0
b = 0
for i in (0..n-1)
    a_t = gets.strip
    row = a_t.split(' ').map(&:to_i)
    a += row[i]
    b += row[n - 1 -i]
end
print (a - b).abs
