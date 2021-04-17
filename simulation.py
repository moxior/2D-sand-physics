import random, time, replit


class Cell:
    def __init__(self, id="Empty"):
        self.id = id
        self.Position = [0, 0]
        self.Rendered = False
        if id == "Empty":
            self.Icon = "⬜"
        elif id == "Brick":
            self.Icon = "⬛"

    def __repr__(self):
        return self.Icon


class Table:
    def __init__(self, tableSize=5):
        def constructTable():
            table = []
            for y in range(tableSize):
                row = []
                for x in range(tableSize):
                    cell = Cell()
                    cell.Position = [x, y]
                    #modify any attrs about the 'Cell' object

                    row.append(cell)

                table.append(row)

            return table

        self.Table = constructTable()
        self.tableSize = tableSize

    def cellExists(self, pos: list):
        y, x = pos[1], pos[0]
        if 0 <= y < self.tableSize and 0 <= x < self.tableSize: return True
        return False

    def moveCell(self, cell, newPosition):
        y, x = cell.Position[1], cell.Position[0]
        placeholder = Cell()
        if not [x, y] == [newPosition[0], newPosition[1]]:
            self.Table[y][x] = placeholder
        self.Table[newPosition[1]][newPosition[0]] = cell
        cell.Position = newPosition

    def getCell(self, pos):
        return self.Table[pos[1]][pos[0]]

    def renderCellDownwards(self, cell):
        y, x = cell.Position[1], cell.Position[0]
        if self.cellExists([x, y + 1]) and self.getCell([x, y + 1
                                                         ]).id == "Empty":
            self.moveCell(cell, [x, y + 1])
        elif self.cellExists([x + 1, y + 1]) and self.getCell(
            [x + 1, y + 1]).id == "Empty":
            self.moveCell(cell, [x + 1, y + 1])

        elif self.cellExists([x - 1, y + 1]) and self.getCell(
            [x - 1, y + 1]).id == "Empty":
            self.moveCell(cell, [x - 1, y + 1])
        else:
            pass

    def render(self):
        for row in self.Table:
            for cell in row:
                cell.Rendered = False


def main():
    grid = Table(15)
    renderStep = 0.20
    c = 0
    while True:
        c += 1
        if c % 4 == 0:
            brick = Cell("Brick")

            grid.moveCell(brick, [7, 0])

        for row in grid.Table:
            print(*row)

        time.sleep(renderStep)
        replit.clear()
        a = 0
        for row in grid.Table:
            for cell in row:
                if cell.id == "Brick" and not cell.Rendered:
                    grid.renderCellDownwards(cell)
                    cell.Rendered = True

        grid.render()


main()
