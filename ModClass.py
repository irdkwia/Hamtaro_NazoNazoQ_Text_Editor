#Transcode code in a text more understandable
def GetSel(ListCode):
	Str = " ノハバパヒビピフブプへべぺホボポマミムメモャヤュユョヨラリルレ !ヲンヴ%&\"()・+,-./0123456789:;。='?-ABCDEFGHIJKLMNOPQRSTUVWXYZ[¥]「」~abcdefghijklmnopqrstuvwxyzトドナニヌネぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらリるれろ…わロワをんァアィイゥウェエォオ力ガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテヂ"
	Sel = ""
	NextFF = False
	NextFE = False
	for Nb in ListCode:
		try:
			if not NextFF and not NextFE:
				if Nb==255:
					NextFF = True
				elif Nb==254:
					NextFE = True
				elif Nb==0:
					Sel+="|n00|"
				else:
					Sel+=Str[Nb]
			elif NextFF:
				NextFF = False
				if Nb==0:
					Sel+="\n"
				elif Nb==1:
					Sel+="|Next|"
				elif Nb==11:
					Sel+="|Start|"
				elif Nb==12:
					Sel+="|Pause|"
				elif Nb==17:
					Sel+="|End|"
				elif Nb==32:
					Sel+="|Black|"
				elif Nb==35:
					Sel+="|Red|"
				elif Nb==38:
					Sel+="|Blue|"
				else:
					Sel+="|x"+str(Nb)+"|"
			else:
				NextFE = False
				if Nb==13:
					Sel+="太"
				elif Nb==14:
					Sel+="郎"
				else:
					Sel+="|c"+str(Nb)+"|"
				
		except:
			Sel+="|n"+str(Nb)+"|"
	return Sel

#Transcode text in code used by the game.
def GetCode(StrConv):
	Str = "²ノハバパヒビピフブプへべぺホボポマミムメモャヤュユョヨラリルレ !ヲンヴ%&\"()・+,-./0123456789:;。='?-ABCDEFGHIJKLMNOPQRSTUVWXYZ[¥]「」~abcdefghijklmnopqrstuvwxyzトドナニヌネぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらリるれろ…わロワをんァアィイゥウェエォオ力ガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテヂ"
	SpecInstr = ""
	ListCode = b''
	for Lettre in StrConv:
		try:
			if Lettre=="\n":
				ListCode += b'\xff\x00'
			elif Lettre=="|" and SpecInstr=="":
				SpecInstr = "|"
			elif Lettre=="|":
				SpecInstr += "|"
				if SpecInstr=="|Black|":
					ListCode += b'\xff\x20'
				elif SpecInstr=="|Red|":
					ListCode += b'\xff\x23'
				elif SpecInstr=="|Blue|":
					ListCode += b'\xff\x26'
				elif SpecInstr=="|Next|":
					ListCode += b'\xff\x01'
				elif SpecInstr=="|Start|":
					ListCode += b'\xff\x0b'
				elif SpecInstr=="|Pause|":
					ListCode += b'\xff\x0c'
				elif SpecInstr=="|End|":
					ListCode += b'\xff\x11'
				else:
					if SpecInstr[1]=="c":
						try:
						       ListCode += bytes([254, int(SpecInstr[2:-1])])
						except:pass
					elif SpecInstr[1]=="n":
						try:
						       ListCode += bytes([int(SpecInstr[2:-1])])
						except:pass
					else:
						try:
						       ListCode += bytes([255, int(SpecInstr[2:-1])])
						except:pass
				SpecInstr = ""
			elif SpecInstr=="":
				ListCode += bytes([Str.index(Lettre)])
			else:
				SpecInstr+=Lettre
		except:
			ListCode+=bytes([32])
	return ListCode
