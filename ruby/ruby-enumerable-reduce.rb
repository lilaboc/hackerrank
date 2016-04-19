# https://www.hackerrank.com/challenges/ruby-enumerable-reduce
# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_terms(n)
  (1..n).inject(0){|product, n| product + n * n + 1}
end
