describe ConstrainedTowers do
  it 'generates ternary numbers' do
    expect(ConstrainedTowers.ternarise 19, 5).to eq '00201'
  end

  context 'diffing ternary numbers' do
    specify 'easy case' do
      expect(Towers.diff '001', '002').to eq 0
    end

    specify 'trickier case' do
      expect(Towers.diff '012', '020').to eq 1
    end
  end
  context 'adjacent stacks' do
    context 'noddy cases' do
      it 'moves from left to centre' do
        stacks = [[], [], []]
        expect(ConstrainedTowers.find_adjacent_stack 0, 0, stacks).to eq 1
      end

      it 'moves from right to centre' do
        stacks = [[], [], []]
        expect(ConstrainedTowers.find_adjacent_stack 0, 2, stacks).to eq 1
      end
    end
  end

  it 'follows the rules' do
    towers = ConstrainedTowers.new 4

    until towers.solved do
      towers.move
      towers.stacks.each do |stack|
        expect(stack.sort.reverse).to eq stack
      end
    end
  end
end
