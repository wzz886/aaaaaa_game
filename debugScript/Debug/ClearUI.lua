-- **********************************************************************
-- Copyright (c) Lakoo
-- File     : ClearUI.lua
-- Author   : WZZ
-- Created  :
-- Purpose  : easy to develop the game
-- **********************************************************************

ClearUI = {}


----------------------------------------
-- string split
function ClearUI.main()

	print("--ClearUI---前----")
	for k, v in pairs(package.loaded) do
		if string.find(k, "ClearUI") then
			print(k)
		end
	end
	package.loaded["Debug.ClearUI"] = nil
	_G["ClearUI"] = nil

	collectgarbage("collect")
	-- print("清理自身完毕")
	-- print("清理自ClearUI.main()身完毕")


	print("---ClearUI--后----")
	for k, v in pairs(package.loaded) do
		if string.find(k, "ClearUI") then
			print(k)
		end
	end
end


ClearUI.main()


