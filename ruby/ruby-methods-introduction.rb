# https://www.hackerrank.com/challenges/ruby-methods-introduction
# Enter your code here. Read input from STDIN. Print output to STDOUT
def prime?(n)
  return false if n == 1
  (2..Math.sqrt(n)).to_a.none? {|i| n % i == 0}
end

#puts prime?(1)
#puts prime?(2)
#puts prime?(3)
#puts prime?(17)
#puts prime?(22)
