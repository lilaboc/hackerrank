# https://www.hackerrank.com/challenges/ruby-enumerable-each-with-index
# Enter your code here. Read input from STDIN. Print output to STDOUT
def skip_animals(animals, skip)
  result = []
  animals.each_with_index do |item, index|
    result.push("#{index}:#{item}") if index >= skip
  end
  result
end
