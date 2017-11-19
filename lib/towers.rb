class Towers
  attr_reader :count, :stacks, :binary

  def initialize discs
    @discs = discs
    @count = 0
    @binary = Towers.binarise @count, @discs
    @stacks = [(0...discs).to_a.reverse, [], []]
  end

  def move
    flip = Towers.diff Towers.binarise(@count, @discs), Towers.binarise(@count += 1, @discs)

    @stacks[1].push @stacks[0].pop
  end

  def binary
    Towers.binarise @count, @discs
  end

  def Towers.binarise value, width
    '%0*b' % [width, value]
  end

  def Towers.diff first, second
    first.chars.reverse.each_with_index do |bit, index|
      if bit == '0' and second.chars.reverse[index] == '1'
        return index
      end
    end
  end
end
