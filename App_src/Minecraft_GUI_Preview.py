from Minecraft_GUI_Dependancies import *
from mine import *

GLASS = block.Block( 20, 0 )

prevImportBlocks = []
prevCircleBlocks = []
prevCubeBlocks = []


def IsBlockPreviewable( ID ):
	if ID == 0:
		return False
	if ID == 6:
		return False
	if ID == 10 or ID == 11 or ID == 51:
		return False
	if ID == 18 or ID == 31 or ID == 32:
		return False
	if ID == 26:
		return False
	if ID == 27 or ID == 28:
		return False
	if ID == 30:
		return False
	if ID == 33 or ID == 34:
		return False
	if ID == 37 or ID == 38 or ID == 39 or ID == 40:
		return False
	if ID == 50:
		return False
	if ID == 52:
		return False
	if ID == 54:
		return False
	if ID == 55:
		return False
	if ID == 64:
		return False
	return True


def SetPrevBlockCircle( x, y, z ):
	global prevCircleBlocks
	if GV.mc.getBlock( x, y, z ) != BEDROCK:
		GV.mc.setBlock( x, y, z, GLASS )
		prev = SecBlock( x, y, z, 20, 0 )
		prevCircleBlocks.append( prev )

def SetPrevBlockCube( x, y, z ):
	global prevCubeBlocks
	if GV.mc.getBlock( x, y, z ) != BEDROCK:
		GV.mc.setBlock( x, y, z, GLASS )
		prev = SecBlock( x, y, z, 20, 0 )
		prevCubeBlocks.append( prev )

def PreviewImport( name ):
	global prevImportBlocks

	if len( prevImportBlocks ) == 0:
		try:
			x1, y1, z1 = GV.mc.player.getTilePos( )
			y, z = 0, 0
			with open( name, 'r' )  as file:
				lines = file.readlines( )
				f1, f2, f3 = 0, 0, 0
				for line in lines:
					if "f" in line:
						f1 = int( line.split( " " )[1] )
						f2 = int( line.split( " " )[2] )
						f3 = int( line.split( " " )[3] )
					elif "*" in line:
						y = y + 1
						z = 0
					else:
						for x in range( len( line.split( " " ) ) - 1 ):
							copyBlock = line.split( " " )[x]
							ID = int( copyBlock.split( ',' )[0] )
							if IsBlockPreviewable( ID ):
								GV.mc.setBlock( x1 + x, y1 + y, z1 + z, block.Block( 20, 0 ) )
								prev = SecBlock( x1 + x, y1 + y, z1 + z, 20, 0 )
								prevImportBlocks.append( prev )
						z = z + 1
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )
	else:
		try:
			for blk in prevImportBlocks:
				GV.mc.setBlock( blk.x, blk.y, blk.z, block.Block( 0 ) )
			prevImportBlocks = []
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )


def PreviewCircle( x, y, z, r, fill ):
	global prevCircleBlocks
	x, y, z = x.get( ), y.get( ), z.get( )
	r = r.get( )
	fill = fill.get( )

	if len( prevCircleBlocks ) == 0:
		if r >= 0:
			try:
				if fill == 0:
					if r == 0:
						if GV.mc.getBlock( x, y, z ) != 7:
							GV.mc.setBlock( x, y, z, block.Block( 20, 0 ) )
					else:

						x2, z2 = r, 0
						while x2 > z2:
							SetPrevBlockCircle( x + x2, y, z + z2 )
							SetPrevBlockCircle( x - x2, y, z + z2 )
							SetPrevBlockCircle( x + x2, y, z - z2 )
							SetPrevBlockCircle( x - x2, y, z - z2 )
							z2 = z2 + 1
							x2 = int ( sqrt( r**2 - z2**2 ) )

						x2, z2 = 0, r
						while z2 > x2:
							SetPrevBlockCircle( x + x2, y, z + z2 )
							SetPrevBlockCircle( x - x2, y, z + z2 )
							SetPrevBlockCircle( x + x2, y, z - z2 )
							SetPrevBlockCircle( x - x2, y, z - z2 )
							x2 = x2 + 1
							z2 = int ( sqrt( r**2 - x2**2 ) )

				else:
					for x2 in range( r + 1 ):
						for z2 in range( r + 1 ):
							if ( x2**2 + z2**2 ) <= r**2:
								SetPrevBlockCircle( x + x2, y, z + z2 )
								SetPrevBlockCircle( x - x2, y, z + z2 )
								SetPrevBlockCircle( x + x2, y, z - z2 )
								SetPrevBlockCircle( x - x2, y, z - z2 )
			except Exception as e:
				if DEBUG:
					print e
				tkMessageBox.showerror( "Error", "Connection lost !" )
				for button in btn:
					button.configure( state = DISABLED )
	else:
		try:
			for blk in prevCircleBlocks:
				GV.mc.setBlock( blk.x, blk.y, blk.z, block.Block( 0 ) )
			prevCircleBlocks = []
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )


def PreviewCube( x1, x2, y1, y2, z1, z2 ):
	global prevCubeBlocks
	if len( prevCubeBlocks ) == 0:
		xs, xf = int( x1.get( ) ), int( x2.get( ) )
		ys, yf = int( y1.get( ) ), int( y2.get( ) )
		zs, zf = int( z1.get( ) ), int( z2.get( ) )

		if xs > xf:
			xs, xf = xf, xs
		if ys > yf:
			ys, yf = yf, ys
		if zs > zf:
			zs, zf = zf, zs
		
		ID = int( blkID.get( ) )
		data = int( blkData.get( ) )

		try:
			for xi in range( xs, xf + 1 ):
				for yi in range( ys, yf + 1 ):
					for zi in range( zs, zf + 1 ):
						SetPrevBlockCube( xi, yi, zi )
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )
	else:
		try:
			for blk in prevCubeBlocks:
				GV.mc.setBlock( blk.x, blk.y, blk.z, block.Block( 0 ) )
			prevCircleBlocks = []
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )