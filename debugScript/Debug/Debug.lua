-- **********************************************************************
-- Copyright (c) Lakoo
-- File     : Debug.lua
-- Author   : WZZ
-- Created  : 2020-12-28
-- Purpose  : easy to develop the game
-- **********************************************************************

Debug = {}

--str是需要查分的对象 d是分界符
local function stringSplit(str, delimiter)
    if not str then
        return 0
    end
    delimiter = delimiter or ","
    local lst = { }
    local n = string.len(str) or 0
    local start = 1
    while start <= n do
        local i = string.find(str, delimiter, start) -- find 'next' 0
        if i == nil then
            table.insert(lst, string.sub(str, start, n))
            break
        end
        table.insert(lst, string.sub(str, start, i-1))
        if i == n then
            table.insert(lst, "")
            break
        end
        start = i + 1
    end
    return lst
end

function Debug.main()
 --        require "Config/ItemConfig"
 --        require "Controller/InitController"

 --        EventManager:sendMsg(EVENT.PLAYER.OPEN_MAIN_VEIW, { player_switch = PLAYER_SWITCH.BAG, player_bag_type_switch = PLAYER_BAG_TYPE_SWITCH.ALL})


	-- if 1 == 1 then return end

	print("-------开始清理 --请等待提示结束---")
	require "Common/CommonFunc"
	require "Common/inspect"

	local ui_map = {}
	local controller_map = {}
	for k, v in pairs(package.loaded) do
		local tab = stringSplit(k, "%.")
		if tab[1] == "UI" then
			ui_map[k] = tab[#tab]
		elseif tab[1] == "Controller" then
			controller_map[k] = tab[#tab]
		end
	end

	print("------关闭界面---------")

	local show_controller_map = {}
	if ControllerManager and ControllerManager.info then
		for name, ctrl in pairs(ControllerManager.info) do
			if ctrl.destoryWindow and ctrl.window then
				ctrl:destoryWindow()
			elseif ctrl.destoryObj and ctrl.uiobj then
				-- 测试手动加obj时会直接调用差生obj,故要清
				ctrl:destoryObj()
			end
			ctrl.data = nil -- 数据不要清
			ctrl:destory()
			ControllerManager.info[name] = nil
			show_controller_map[name] = true
		end
	end

	-- 界面引用
	if UIManager then
		UIManager.ui_windows = {}
		UIManager.window_info = {}
	end


	print("------清理---全局变量-----")
	for _, map in ipairs({ui_map, controller_map}) do
		for path_name, g_name in pairs(map) do
			package.loaded[path_name] = nil
			_G[g_name] = nil
			print("--path:" .. path_name .. "  class name:"..g_name)
		end
	end

	package.loaded["Debug.Debug"] = nil
	_G["Debug"] = nil

	collectgarbage("collect")
	collectgarbage("collect")
	print("------------------开始结束-------------")

	-------------------------
	-- 初始已经加载的controller
	require "Controller/ControllerManager"
	local ControllerManager = ControllerManager
	print(show_controller_map, ControllerManager)
	for name in pairs(show_controller_map or {}) do
		print("---重新加载controller:", name)
		ControllerManager:getInfo(name)
	end

	-- local controller = ControllerManager:getInfo("MainController")
	-- controller:openWindow()

	-- 物品技能快建设置
	-- local controller = ControllerManager:getInfo("PlayerHotKeyController")
	-- local item = controller:createObjUI(UIManager.ui_root)

	-- 打开背包界面
	EventManager:sendMsg(EVENT.PLAYER.OPEN_MAIN_VEIW, { player_switch = PLAYER_SWITCH.BAG, player_bag_type_switch = PLAYER_BAG_TYPE_SWITCH.ALL})

end

Debug.main()


