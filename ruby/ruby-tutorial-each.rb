# https://www.hackerrank.com/challenges/ruby-tutorial-each
# Enter your code here. Read input from STDIN. Print output to STDOUT
def scoring(array)
  array.each {|user| user.update_score }
end
