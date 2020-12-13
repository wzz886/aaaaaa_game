-- **********************************************************************
-- Copyright (c) Lakoo
-- File     : MainSkillTestUI.lua
-- Author   : WZZ
-- Created  : 2020-12-11
-- Purpose  : mainui test scroll view
-- **********************************************************************


require "UI/MainUI/MainSkillTestItemUI"
MainSkillTestUI = class("MainSkillTestUI", UIWindow)

-- scrill cell w and h
local CELL_W, CELL_H = 540, 120

----------------------------------------
-- ctor
function MainSkillTestUI:ctor()
    self.super:ctor()

    self.ui = {}
end


----------------------------------------
-- destory self & register function
function MainSkillTestUI:destory()
    UIWindow.destory(self)

    local ui = self.ui
    if ui.close_btn_click_func then
        LuaToCSharp.RemoveButtonOnClick(ui.close_btn_right, ui.close_btn_click_func)
    end

    self.ui      = nil
    self.control = nil
end


----------------------------------------
-- get user define ui object
function MainSkillTestUI:initUIObject()
    local ui = {}

	ui.close_btn_right = LuaToCSharp.GetUIButton(self.object, "bg_img/close_btn")
	ui.Text = LuaToCSharp.GetUIText(self.object, "bg_img/Text")

	ui.main_scroll_obj  = LuaToCSharp.GetGameObject(self.object, "bg_img/scroll")
	ui.main_scroll_rect = LuaToCSharp.GetScrollRect(ui.main_scroll_obj)
	ui.main_scroll_ui   = LuaToCSharp.GetUIScrollRect(ui.main_scroll_obj, "Viewport/Content")
    ui.close_btn_click_func = UnityEngine.Events.UnityAction(
        function()
            UIManager:destoryWindow("MainSkillTestUI")
        end)
    LuaToCSharp.AddButtonOnClick(ui.close_btn_right, ui.close_btn_click_func)

    self.ui = ui
end


----------------------------------------
-- init ui callback
function MainSkillTestUI:initCallBack()
	local info = {}
	for i = 1, 30 do
		info[i] = {desc = "这是第" .. i .. "个", index = i}
	end

	self:updateList(info)
end


----------------------------------------
-- update list
function MainSkillTestUI:updateList(info)
	self.ui.Text.text = "000000000"

	print(self.ui.main_ui_scroll)
	print(self.ui.main_scroll)
	print(self.ui.main_scroll_obj)

	local display_count = LuaToCSharp.InitUIScrollRect(self.ui.main_scroll_ui, self.ui.main_scroll_rect,
		CELL_W, CELL_H, #info,
		function(data_index, item_index)
			-- if self.update_server_info_ui ~= nil then
			-- 	self.update_server_info_ui(self.control, data_index + 1, item_index + 1)
			-- end
			print("-----", data_index, item_index)
			self:updateItem(info[data_index], item_index)
		end
	)

	for i = 1, display_count do
		local item = MainSkillTestItemUI.new("mainui_skill_test_item",
			function()
				LuaToCSharp.AddUIScrollItem(self.ui.main_scroll_uil, item.object)
				item:setData(info[i])
				self.item_list[#self.item_list + 1] = item
			end)
	end
end


----------------------------------------
-- update list item
function MainSkillTestUI:updateItem(data, item_index)
	print(data_index, item_index)

	local item = self.item_list[item_index]
	if not item then end

	item:setData(data)
end
