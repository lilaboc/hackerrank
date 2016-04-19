# https://www.hackerrank.com/challenges/ruby-enumerable-group-by
# Enter your code here. Read input from STDIN. Print output to STDOUT
def group_by_marks(marks, n)
  marks.group_by {|name, mark| mark  < n ? "Failed" : "Passed"}
end



