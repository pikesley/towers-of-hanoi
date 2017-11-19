describe Towers do
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

  it 'diffs two binary numbers' do
    expect(Towers.diff '000', '001').to eq 0
    expect(Towers.diff '001', '010').to eq 1
  end
end
