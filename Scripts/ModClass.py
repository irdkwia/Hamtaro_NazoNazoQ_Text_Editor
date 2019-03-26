LISTCHAR = chr(0)+"ノハバパヒビピフブプへべぺホボポマミムメモャヤュユョヨラリルレ !ヲンヴ%&\"()・+,-./0123456789:;。='?-ABCDEFGHIJKLMNOPQRSTUVWXYZ[¥]「」~abcdefghijklmnopqrstuvwxyzトドナニヌネぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらリるれろ…わロワをんァアィイゥウェエォオ力ガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデ"
LISTCHARSPEC = "↑→↓←ⒶⒷⓍⓎⓇⓁ♥♪★太郎○✕"

#Transcode code in a text more understandable
def GetSel(ListCode):
	Sel = ""
	NextFF = False
	NextFE = False
	NextEndSpec = False
	for Nb in ListCode:
		try:
			if not NextFF and not NextFE and not NextEndSpec:
				if Nb==255:
					NextFF = True
				elif Nb==254:
					NextFE = True
				elif Nb==0:
					Sel+="|n00|"
				else:
					Sel+=LISTCHAR[Nb]
			elif NextEndSpec:
                                NextEndSpec = False
                                Sel+=str(Nb)+"|"
			elif NextFF:
				NextFF = False
				if Nb==0:
					Sel+="|NL|"
				elif Nb==1:
					Sel+="|Next:"
					NextEndSpec = True
				elif Nb==11:
					Sel+="|Start:"
					NextEndSpec = True
				elif Nb==12:
					Sel+="|Pause:"
					NextEndSpec = True
				elif Nb==17:
					Sel+="|End:"
					NextEndSpec = True
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
				try:
					Sel+=LISTCHARSPEC[Nb]
				except:
					Sel+="|c"+str(Nb)+"|"
				
		except:
			Sel+="|n"+str(Nb)+"|"
	return Sel

#Transcode text in code used by the game.
def GetCode(LISTCHARConv):
	SpecInstr = ""
	ListCode = b''
	for Lettre in LISTCHARConv:
		try:
			if Lettre=="|" and SpecInstr=="":
				SpecInstr = "|"
			elif Lettre=="|":
				SpecInstr += "|"
				Split = SpecInstr.split(":")
				OKSP = False
				if SpecInstr.lower()=="|black|":
					ListCode += b'\xff\x20'
				elif SpecInstr.lower()=="|red|":
					ListCode += b'\xff\x23'
				elif SpecInstr.lower()=="|blue|":
					ListCode += b'\xff\x26'
				elif SpecInstr.upper()=="|NL|":
                                        ListCode += b'\xff\x00'
				elif Split[0].lower()=="|next":
					ListCode += b'\xff\x01'
					OKSP = True
				elif Split[0].lower()=="|start":
					ListCode += b'\xff\x0b'
					OKSP = True
				elif Split[0].lower()=="|pause":
					ListCode += b'\xff\x0c'
					OKSP = True
				elif Split[0].lower()=="|end":
					ListCode += b'\xff\x11'
					OKSP = True
				else:
					if SpecInstr[1].lower()=="c":
						try:
						       ListCode += bytes([254, int(SpecInstr[2:-1])])
						except:pass
					elif SpecInstr[1].lower()=="n":
						try:
						       ListCode += bytes([int(SpecInstr[2:-1])])
						except:pass
					else:
						try:
						       ListCode += bytes([255, int(SpecInstr[2:-1])])
						except:pass
				if OKSP:
                                        try:
                                                ListCode += bytes([int(Split[1][:-1])])
                                        except:
                                                ListCode += bytes([0])
				SpecInstr = ""
			elif SpecInstr=="":
				ListCode += bytes([LISTCHAR.index(Lettre)])
			else:
				SpecInstr+=Lettre
		except:
			try:
				b = bytes(LISTCHARSPEC.index(Lettre))
				ListCode+=b'\xfe'+b
				del b
			except:
				ListCode+=bytes([32])
	return ListCode
