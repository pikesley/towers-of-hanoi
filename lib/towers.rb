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
    source = Towers.find_disc flip, @stacks

    @stacks[Towers.find_stack flip, source, @stacks].push @stacks[source].pop
  end

  def binary
    Towers.binarise @count, @discs
  end

  def solved
    binary.chars.all? { |bit| bit.to_i == 1 }
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

  def Towers.find_disc needle, stacks
    stacks.each_with_index do |stack, index|
      return index if stack.index needle
    end
  end

  def Towers.find_stack disc, source, stacks
    if stacks[(source + 1) % 3] == []
      return (source + 1) % 3
    end

    if stacks[(source + 1) % 3][-1] < disc
      return (source + 2) % 3
    end

    return (source + 1) % 3
  end
end
