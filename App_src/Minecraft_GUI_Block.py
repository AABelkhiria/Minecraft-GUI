from Minecraft_GUI_Dependancies import *

def BlockIData( main ):
	msg = Message( main,'Block Data' )
	msg.place( x = 5, y = -9 )

	frame = Frame( main )
	frame.pack( pady = 10 )

	txtID = Message( frame, 'Block ID' )
	txtID.grid( column = 0, row = 0, padx = 5, pady = 7 )

	ID = Entry( frame )
	ID.grid( column = 1, row = 0, padx = 5 )
	ID.configure( textvariable = blkID )
	ID.configure( width = 3 )

	txtData = Message( frame,'Block Data' )
	txtData.grid( column = 0, row = 1, padx = 5 )

	data = Entry( frame )
	data.grid( column = 1, row = 1, padx = 5 )
	data.configure( textvariable = blkData )
	data.configure( width = 3 )

	chk = Checkbutton( frame )
	chk.grid( column = 0, row = 2, columnspan = 2, padx = 5 )
	chk.configure( variable = destroyB )
	chk.configure( text = 'Destroy on building' )

	chk1 = Checkbutton( frame )
	chk1.grid( column = 0, row = 3, columnspan = 2, padx = 5 )
	chk1.configure( variable = destroyP )
	chk1.configure( text = 'Destroy on Preview' )