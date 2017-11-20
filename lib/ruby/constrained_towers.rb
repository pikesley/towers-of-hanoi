class ConstrainedTowers < Towers
  @@directions = {}

  def initialize discs
    super
    @ternary = ConstrainedTowers.ternarise @count, @discs
  end

  def move
    flip = Towers.diff ConstrainedTowers.ternarise(@count, @discs), ConstrainedTowers.ternarise(@count += 1, @discs)
    source = Towers.find_disc flip, @stacks

    @stacks[ConstrainedTowers.find_adjacent_stack flip, source, @stacks].push @stacks[source].pop
  end

  def binary
    ternary
  end

  def ternary
    ConstrainedTowers.ternarise @count, @discs
  end

  def solved
    ternary.chars.all? { |trit| trit.to_i == 2 }
  end

  def inspect
    {
      stacks: @stacks,
      count: ternary
    }
  end

  def ConstrainedTowers.ternarise value, width
    '%0*d' % [width, value.to_s(3)]
  end

  def ConstrainedTowers.find_adjacent_stack disc, source, stacks
    begin
      direction = @@directions[disc]
    rescue KeyError
      @@directions[disc] = :right
      direction = right
    end

    case source
    when 0
      @@directions[disc] = :right
      return 1
    when 2
      @@directions[disc] = :left
      return 1
    when 1
      if @@directions[disc] == :right
        return 2
      else
        return 0
      end
    end
  end
end
