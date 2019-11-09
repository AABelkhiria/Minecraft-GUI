from App_src.Minecraft_GUI_Dependancies import *

def close( event ):
    root.withdraw( )
    exit( )

root.title( "Minecraft GUI" )
root.configure( background = '#d9d9d9' )
root.resizable( False, False )
root.bind( '<Escape>', close )

style = Style( )
style.theme_use( 'clam' )
style.configure( '.', background = '#d9d9d9' )
style.configure( '.', foreground = '#000000' )
style.configure( '.', font = "TkDefaultFont" )
style.map( '.', background = [ ( 'selected', '#d9d9d9' ), ( 'active', '#d9d9d9' ) ] )

DrawFrames( root )

root.mainloop( )
