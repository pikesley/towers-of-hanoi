describe Towers do
  context 'states' do
    towers = Towers.new 3

    it 'has the correct initial state' do
      expect(towers.binary).to eq '000'
      expect(towers.stacks).to eq [[2, 1, 0], [], []]
    end

    it 'has the correct first state' do
      towers.move
      expect(towers.binary).to eq '001'
      expect(towers.stacks).to eq [[2, 1], [0], []]
    end

    it 'has the correct second state' do
      towers.move
      expect(towers.binary).to eq '010'
      expect(towers.stacks).to eq [[2], [0], [1]]
    end

    it 'has the correct third state' do
      towers.move
      expect(towers.binary).to eq '011'
      expect(towers.stacks).to eq [[2], [], [1, 0]]
    end

    it 'has the correct fourth state' do
      towers.move
      expect(towers.binary).to eq '100'
      expect(towers.stacks).to eq [[], [2], [1, 0]]
    end

    it 'has the correct fifth state' do
      towers.move
      expect(towers.binary).to eq '101'
      expect(towers.stacks).to eq [[0], [2], [1]]
    end

    it 'has the correct sixth state' do
      towers.move
      expect(towers.binary).to eq '110'
      expect(towers.stacks).to eq [[0], [2, 1], []]
    end

    it 'has the correct final state' do
      towers.move
      expect(towers.binary).to eq '111'
      expect(towers.stacks).to eq [[], [2, 1, 0], []]
    end
  end

  context 'knows when to stop' do
    towers = Towers.new 2

    it 'is not done yet' do
      towers.move
      towers.move
      expect(towers.solved).to eq false
    end

    it 'is done now' do
      towers.move
      expect(towers.solved).to eq true
    end
  end

  it 'follows the rules' do
    towers = Towers.new 12

    until towers.solved do
      towers.move
      towers.stacks.each do |stack|
        expect(stack.sort.reverse).to eq stack
      end
    end
  end

  context 'matrices' do
    towers = Towers.new 5

    it 'has the correct initial matrix' do
      expect(towers.matrix).to eq [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
      ]
    end
  end

  it 'diffs two binary numbers' do
    expect(Towers.diff '000', '001').to eq 0
    expect(Towers.diff '001', '010').to eq 1
  end

  it 'locates a given disc' do
    stacks = [[2, 1], [0], []]
    expect(Towers.find_disc 0, stacks).to eq 1
    expect(Towers.find_disc 1, stacks).to eq 0
  end

  context 'locates the next receptive stack' do
    it 'solves the easy case' do
      stacks = [[2], [0], []]
      expect(Towers.find_stack(1, 2, stacks)).to eq 0
    end

    it 'solves a trickier case' do
      stacks = [[], [2], [1]]
      expect(Towers.find_stack(0, 2, stacks)).to eq 0
    end
  end
end
