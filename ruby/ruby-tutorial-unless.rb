# https://www.hackerrank.com/challenges/ruby-tutorial-unless
# Enter your code here. Read input from STDIN. Print output to STDOUT
def scoring(array)
   array.each {|user| user.update_score unless user.is_admin? }
end

