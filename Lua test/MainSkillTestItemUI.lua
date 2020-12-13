-- **********************************************************************
-- Copyright (c) Lakoo
-- File     : MainSkillTestItemUI.lua
-- Author   : WZZ
-- Created  : 2020-12-08
-- Purpose  : 
-- **********************************************************************


require "Framework/LuaUILoadObject"
MainSkillTestItemUI = class("MainSkillTestItemUI", LuaUILoadObject)


----------------------------------------
-- ctor
function MainSkillTestItemUI:ctor(asset_name)
    self.super:ctor()
    self.res_handle = 0
    self:loadResource(asset_name, nil)

    self.ui = {}
end


----------------------------------------
-- destory self & register function
function MainSkillTestItemUI:destory()
    self.super:destory(self)

    if self.res_handle > 0 then
        LuaToCSharp.ClearLoadResource(self.res_handle)
    end


    -- if self.tab_item_list then
    --     for _, item in ipairs(self.tab_item_list) do
    --         item:destory()
    --     end
    -- end

    -- local ui = self.ui
    -- if ui.btn_click_func then
    --     LuaToCSharp.RemoveButtonOnClick(ui.close_btn_right, ui.btn_click_func)
    -- end

    -- self.ui      = nil
    -- self.control = nil
end


----------------------------------------
-- set data
function MainSkillTestItemUI:setData(data)
    self.data = data
end


----------------------------------------
-- get user define ui object
function MainSkillTestItemUI:initUIObject()
    local ui = {}

    ui.desc_txt = LuaToCSharp.GetUIButton(self.object, "desc_txt")
    -- ui.btn_click_func = UnityEngine.Events.UnityAction(
    --     function()
    --         UIManager:destoryWindow("MainSkillTestItemUI")
    --     end)
    -- LuaToCSharp.AddButtonOnClick(ui.close_btn_right, ui.btn_click_func)

    self.ui = ui
end


----------------------------------------
-- init ui callback
function MainSkillTestItemUI:initCallBack()

end
